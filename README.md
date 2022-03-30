## **Visão Geral**

O **trace-app-cs-plugin** foi projetado para apoiar os desenvolvedores a configurar e utilizar o [Opentelemetry](https://opentelemetry.io/) com exporter para [Jaeger](https://www.jaegertracing.io/) e Instrumentação [AWS X-Ray](https://docs.aws.amazon.com/pt_br/xray/latest/devguide/aws-xray.html).

Para aplicar o plugin execute o comando:
```
    $ stk apply plugin skynet-dotnet-stack/trace-app-cs-plugin
```

#### **Pré-requisitos**
Para utilizar esse plugin é necessário ter uma stack dotnet criada pelo cli do StackSpot que você pode baixar [**aqui**](https://stackspot.com.br/).

Ter instalado:
- .NET 5 ou 6 
- O template base de `rest-app-cs-template` já deverá estar aplicado para você conseguir utilizar este plugin. 

#### **Inputs**
Os inputs necessários para utilizar o plugin são:
| **Campo** | **Valor** | **Descrição** |
| :--- | :--- | :--- |
| Port| ex.: 6831 | Porta do Agent com comunicação via UDP  |
| AppName|  ex.: MyAppName | Nome da Aplicação - Campo Obrigatório |
| ExporterType|  Jaeger / X-Ray / OTLP | Tipo de Exportação |
| Host|  ex.: localhost | Hostname do agent - comunicação via UDP |
| ConsoleExporter|  true/false | Indicador para exportar para o console |
| UseGrpcClientInstrumentation|  true/false | Indicador para habilitar instrumentação gRPC |
| UseHttpClientInstrumentation|  true/false | Indicador para habilitar instrumentação http |
| Tags|  ex.: X-PTO-TraceID, X-PTO-ParentSpanId | Headers que serão propagados |

Você pode configurar as variáveis no arquivo `appsettings.json`.

```json
{
  "AppName": "MyAppName",  
  "Telemetry": {
    "ExporterType": "Jaeger",
    "Host": "127.0.0.1",
    "Port": 6831,
    "ConsoleExporter": true,
    "UseHttpClientInstrumentation": true,
    "UseGrpcClientInstrumentation": true,
    "Tags": [
            "X-PTO-TraceId",
            "X-PTO-ParentSpanId",
            "X-PTO-SpanId"
     ]    
  }
}
```

#### **Configurações**

Adicione ao seu `IServiceCollection` via `services.AddOpenTelemetryTracing()` no `Startup` da aplicação ou `Program`.

```csharp
        public void ConfigureServices(IServiceCollection services)
        {
            services.AddOpenTelemetryTracing(Configuration);
        }
```

#### Ambiente local

Esta etapa não é obrigatória. Execute o comando abaixo para disponibilizar container `jaegertracing`:

```
  docker run -d -p6831:6831/udp -p16686:16686 jaegertracing/all-in-one:latest
```

Para visualizar os traces acesse: http://localhost:16686/
