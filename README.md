- **Descrição:** O plugin trace-app-cs-plugin adiciona em uma stack a capacidade de provisionar o uso de segredos armazenados na AWS trace Manager. 

- **Categoria:** Observability. 
- **Stack:** dotnet.
- **Criado em:** 03/02/2022. 
- **Última atualização:** 03/02/2022.
- **Download:** https://github.com/stack-spot/trace-app-cs-plugin.git.


## **Visão Geral**
### **trace-app-cs-plugin**

O **trace-app-cs-plugin** adiciona em uma stack a capacidade de provisionar o uso de segredos armazenados na AWS trace Manager, reduzindo o risco da exposição de dados sensíveis no código, como logins e senhas de vários tipos (banco de dados, recursos de rede, etc.), chaves de API, chaves de criptografia e similares.

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
- [**Nuget**](https://www.nuget.org/packages/StackSpot.Tracing/)
- [**Nuget**](https://www.nuget.org/packages/StackSpot.Tracing.XRay/)
