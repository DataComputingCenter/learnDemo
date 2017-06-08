using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Text;
using System.Web.Http;

namespace webApiDemo.Controllers
{
    public class ProductController : ApiController
    {

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

        [HttpGet]
        public string FindProduct(int id, int id2) { return "value"; }

        [HttpGet]
        public void GetWith3Param(int id, int id2, int id3)
        {
        }

        [HttpGet]
        public HttpResponseMessage GetBackResp(int id1,int id2,int id3,int id4)
        {
            HttpResponseMessage response = Request.CreateResponse(HttpStatusCode.OK, "love you");
            response.Content = new StringContent("love you wep api", Encoding.Unicode);
            response.Headers.CacheControl = new CacheControlHeaderValue
            {
                MaxAge = TimeSpan.FromSeconds(600)
            };
            return response;
        }


    }
}
