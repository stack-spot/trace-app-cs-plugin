from templateframework.runner import run
from templateframework.template import Template
from templateframework.metadata import Metadata
import subprocess
import json
import os

def put_appsettings(metadata: Metadata, project_name: str, exporter_type: str, file_name: str):
        os.chdir(f'{metadata.target_path}/src/{project_name}.Api/')
        print(f'Setting {file_name}...')

        if exporter_type == 'X-Ray - Daemon':
            if file_name == 'appsettings.json': 
                disable_local = False 
            else: 
                disable_local = True
            config = {
                        "XRay": {
                            "DisableXRayTracing": disable_local,
                            "DaemonAddress": f"{metadata.inputs['server']}:{metadata.inputs['port']}"                            
                        }                
                     }
        else:
            config = {
                        "Telemetry": {
                            "ExporterType": f"{metadata.inputs['exporter_type']}",
                            "Host": f"{metadata.inputs['exporter_type']}",
                            "Port": f"{metadata.inputs['exporter_type']}",
                            "ConsoleExporter": False,
                            "UseHttpClientInstrumentation": True
                        }                
                     }            

        with open(file=file_name, encoding='utf-8-sig', mode='r+') as appsettings_json_file:
            appsettings_json_content = json.load(appsettings_json_file)
            appsettings_json_content.update(config)                                         
            appsettings_json_file.seek(0)
            json.dump(appsettings_json_content, appsettings_json_file, indent=2)
        print(f'Setting {file_name} done.')   


class Plugin(Template):
    def post_hook(self, metadata: Metadata):
        project_name = metadata.global_inputs['project_name']
        exporter_type = metadata.inputs['exporter_type']

        os.chdir(f'{metadata.target_path}/src/{project_name}.Domain/')
        
        if exporter_type == 'X-Ray - Daemon':
            subprocess.run(['dotnet', 'add', 'package', 'StackSpot.Tracing.XRay'])
            using = f"using StackSpot.Tracing.XRay;\n"
            service = f"services.AddXRay(configuration);"
            app = f"app.UseXRay(configuration[\"AppName\"]);"
        else:
            subprocess.run(['dotnet', 'add', 'package', 'StackSpot.Tracing'])
            using = f"using StackSpot.Tracing;\n"
            service = f"services.AddOpenTelemetryTracing(configuration);"

        os.chdir(f'{metadata.target_path}/src/{project_name}.Api/')

        put_appsettings(metadata, project_name, exporter_type, 'appsettings.json')
        put_appsettings(metadata, project_name, exporter_type, 'appsettings.Development.json')         
               
        print('Setting Configuration...')

        configuration_file = open(file='ConfigurationStackSpot.cs', mode='r')
        content = configuration_file.readlines()
        index = [x for x in range(len(content)) if 'return services' in content[x].lower()]
        content[0] = using+content[0]
        content[index[0]] = f"{service}\n{content[index[0]]}"

        if exporter_type == 'X-Ray - Daemon':
            index_app = [x for x in range(len(content)) if 'return app' in content[x].lower()]            
            content[index_app[0]] = f"{app}\n{content[index_app[0]]}"     
        
        configuration_file = open(file='ConfigurationStackSpot.cs', mode='w')                     
        configuration_file.writelines(content)
        configuration_file.close()

        print('Setting Configuration done.') 

        print('Apply dotnet format...')
        os.chdir(f'{metadata.target_path}/')
        subprocess.run(['dotnet', 'format', './src'])   
        print('Apply dotnet format done...')

if __name__ == '__main__':
    run(Plugin())