- **Descrição:** O trace-app-cs-plugin foi projetado para apoiar os desenvolvedores a configurar e utilizar o Opentelemetry com exporter para Jaeger e Instrumentação AWS X-Ray.

- **Categoria:** Observability. 
- **Stack:** dotnet.
- **Criado em:** 03/02/2022. 
- **Última atualização:** 03/02/2022.
- **Download:** https://github.com/stack-spot/trace-app-cs-plugin.git.


## **Visão Geral**
### **trace-app-cs-plugin**

O **trace-app-cs-plugin** foi projetado para apoiar os desenvolvedores a configurar e utilizar o Opentelemetry com exporter para Jaeger e Instrumentação AWS X-Ray.

## **Uso**

### **Pré-requisitos**
Para utilizar esse plugin, é necessário ter uma stack dotnet criada pelo cli.

### **Instalação**
Para fazer o download do **trace-app-cs-plugin**, siga os passos abaixo:

**Passo 1.** Copie e cole a URL abaixo no seu navegador/terminal:
```
https://github.com/stack-spot/trace-app-cs-plugin.git
```

## **Configuração**

### **Inputs**
Os inputs necessários para utilizar o plugin são:
| **Campo** | **Valor** | **Descrição** |
| :--- | :--- | :--- |
| Type| Padrão: "Jaeger" | Tipo do Exporter(Jaeger, OTLP, X-Ray, X-Ray - Daemon) |
| Server|  | Hostname do agent  |
| Port|  | Port do agent  |

### **Exemplo de uso**
- [**Nuget OpenTelemetry**](https://www.nuget.org/packages/StackSpot.Tracing/)
- [**Nuget X-Ray**](https://www.nuget.org/packages/StackSpot.Tracing.XRay/)
