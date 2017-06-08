# asp.net WebApi 

## Devops工具
* unit test

* js ajax

* fiddler

* vs 2017 Community

* msbuilder

* vscode

## 简介
* rest服务

* 与Wcf、WebService、Rpc比较

* http协议

* 特性
           
           先进的 HTTP 编程模型
           支持路由
           内容协商
           模型绑定与验证
           过滤 
           查询聚合
           改进的 Http 细节可测试性
           改进的依赖反转 (IoC) 支持
           基于代码的配置
           自托管 (Self-Host) 

## 创建Asp.net WebAPI iis 宿主
> vs 2017 中创建WebAPI

> 添加webApiConfig类
```
public static class WebApiConfig
    {
        public static void Register(HttpConfiguration config)
        {
            // Web API configuration and services

            // Web API routes
            config.MapHttpAttributeRoutes();

            config.Routes.MapHttpRoute(
                name: "DefaultApi",
                routeTemplate: "api/{controller}/{id}",
                defaults: new { id = RouteParameter.Optional }
            );
        }
    }
```
>添加 ApiController
```
public class ValuesController : ApiController
    {
        // GET api/values
        public IEnumerable<string> Get()
        {
            return new string[] { "value1", "value2" };
        }

        // GET api/values/5
        public string Get(int id)
        {
            return "value";
        }

        // POST api/values
        public void Post([FromBody]string value)
        {
        }

        // PUT api/values/5
        public void Put(int id, [FromBody]string value)
        {
        }

        // DELETE api/values/5
        public void Delete(int id)
        {
        }
    }
```

>启动 startUp

>调用- Get

>调用- Fiddler

## Asp.net WebApi 路由和action

### 路由
> 路由表
```
            // Web API routes
            config.MapHttpAttributeRoutes();

            config.Routes.MapHttpRoute(
                name: "DefaultApi",
                routeTemplate: "api/{controller}/{id}",
                defaults: new { id = RouteParameter.Optional }
            );
```
> 路由变化
```
        [HttpGet]
        public string FindProduct(int id) { return "value"; }
```
> 启用属性路由
```
config.MapHttpAttributeRoutes(); 
```
> 路由属性
```
        [Route("api/SddLxQdModelOper")]
        public IEnumerable<string> Get()
        {
            return new string[] { " SddLxQdModelOper", " SddLxQdModelOper" };
        }
```

### action
> action
```
        // GET: api/Product
        public IEnumerable<string> Get()
        {
            return new string[] { "value1", "value2" };
        }

        // GET: api/Product/5
        public string Get(int id)
        {
            return "value";
        }

        // POST: api/Product
        public void Post([FromBody]string value)
        {
        }

        // PUT: api/Product/5
        public void Put(int id, [FromBody]string value)
        {
        }

        // DELETE: api/Product/5
        public void Delete(int id)
        {
        }
```
> action 路由,参见路由章节：

> action 返回值

    1.void
    2.HttpResponseMessage
    3.IHttpActionResult
    4.其它类型

   > void
   ```
        [HttpGet]
        public void GetWith3Param(int id, int id2, int id3)
        {
        }
   ```
   > HttpResposeMessage
   ```
   public HttpResponseMessage GetBackResp()
        {
            HttpResponseMessage response = Request.CreateResponse(HttpStatusCode.OK, "love you");
            response.Content = new StringContent("love you wep api", Encoding.Unicode);
            response.Headers.CacheControl = new CacheControlHeaderValue
            {
                MaxAge = TimeSpan.FromSeconds(600)
            };
            return response;
        }
   ```
   > IHttpActionResult
   ```
        // GET api/SddLxQdModelOper/5
        [Route("api/SddLxQdModelOper")]
        public IHttpActionResult Get(string properties)
        {
            LogHelper.Info("SddLxQdModelOper Start");
            JObject result = null;
            LxqdJobModel jobModel = CreateJobModel(properties);
            if (jobModel == null)
                throw new ArgumentNullException("properties");
            result = SddLxQdModelOperHandler(jobModel);
            LogHelper.Info("SddLxQdModelOper Get end");
            return Json(result);
        }
   ```

   > 其它返回类型
   ```
   public Product GetProductById( int id)
        {
            Product product = repository.GetProductById(id);
            if (product==null )
                throw new HttpResponseException ( HttpStatusCode.NotFound);
 
            return product;
        }
   ```


## Asp.NET WebApi 跨域
> nuget Microsoft.AspNet.WebApi.Cors

> WebApiConfig.Register方法中加入代码
```
config.EnableCors();

```
> 在Controller上加上Attribute,可选
```
[EnableCors(origins: "*", headers: "*", methods: "*")]
```

> 跨域调用

> ajax 调用

> flex调用，需要调用跨域文件，将文件放在iis下面

## 自宿主的WebAPI

> Create a Console Application

> Add the Web API and OWIN Packages

> Install-Package Microsoft.AspNet.WebApi.OwinSelfHost

> Startup

```
using Owin; 
using System.Web.Http; 

namespace OwinSelfhostSample 
{ 
    public class Startup 
    { 
        // This code configures Web API. The Startup class is specified as a type
        // parameter in the WebApp.Start method.
        public void Configuration(IAppBuilder appBuilder) 
        { 
            // Configure Web API for self-host. 
            HttpConfiguration config = new HttpConfiguration(); 
            config.Routes.MapHttpRoute( 
                name: "DefaultApi", 
                routeTemplate: "api/{controller}/{id}", 
                defaults: new { id = RouteParameter.Optional } 
            ); 

            appBuilder.UseWebApi(config); 
        } 
    } 
}
```
> API Controller
```
using System.Collections.Generic;
using System.Web.Http;

namespace OwinSelfhostSample 
{ 
    public class ValuesController : ApiController 
    { 
        // GET api/values 
        public IEnumerable<string> Get() 
        { 
            return new string[] { "value1", "value2" }; 
        } 

        // GET api/values/5 
        public string Get(int id) 
        { 
            return "value"; 
        } 

        // POST api/values 
        public void Post([FromBody]string value) 
        { 
        } 

        // PUT api/values/5 
        public void Put(int id, [FromBody]string value) 
        { 
        } 

        // DELETE api/values/5 
        public void Delete(int id) 
        { 
        } 
    } 
}
```

 > Start the OWIN Host

 ```
 using Microsoft.Owin.Hosting;
using System;
using System.Net.Http;

namespace OwinSelfhostSample 
{ 
    public class Program 
    { 
        static void Main() 
        { 
            string baseAddress = "http://localhost:9000/"; 

            // Start OWIN host 
            using (WebApp.Start<Startup>(url: baseAddress)) 
            { 
                // Create HttpCient and make a request to api/values 
                HttpClient client = new HttpClient(); 

                var response = client.GetAsync(baseAddress + "api/values").Result; 

                Console.WriteLine(response); 
                Console.WriteLine(response.Content.ReadAsStringAsync().Result); 
                Console.ReadLine(); 
            } 
        } 
    } 
 }
 ```

 > Make a Request Using HttpClient
 ```
 using System;
using System.Net.Http;

namespace OwinSelfhostSample 
{ 
    public class Program 
    { 
        static void Main() 
        { 
            string baseAddress = "http://localhost:9000/"; 
            // Create HttpCient and make a request to api/values 
            HttpClient client = new HttpClient(); 

            var response = client.GetAsync(baseAddress + "api/values").Result; 

            Console.WriteLine(response); 
            Console.WriteLine(response.Content.ReadAsStringAsync().Result); 
            Console.ReadLine(); 
        } 
    } 
 }
 ```

## 其他高级技术
* 同步异步
* 异常捕获
* 自定义参数
* 状态码
* ........

## 模型计算服务

> 模型管理引擎的所有Rest服务
