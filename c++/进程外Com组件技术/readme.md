## 一，创建一个进程外com组件
1. 打开VS2010，点击File->New->Project，选择Atl->Atl Project，输入工程名MyComTest，确认后点击Next。
 
2. 注意选择第二项Executable(EXE)，完成。
    Dynamic Link Library(DLL) 表示建立一个 DLL 的组件程序（进程内组件）。
    Executable(EXE) 表示建立一个 EXE 的组件程序（进程外组件）。
Service(EXE) 表示建立一个服务程序，系统启动后就会加载并执行的程序。
 
3. 注意选择第二项Executable(EXE)，完成。
4. 工程上右击Add->Class，界面上选择Atl Simple Object，点击Add。
 
5. 界面上输入Short name以及ProgID（工程名.类名），Next。
 
6. 注意界面上Aggregation选择No，完成。
 
7. 现在我们有了一个空的接口，里面需要添加方法供端上调用。打开类视图，在刚才创建的对外的接口ITest上右击Add->Add Method。
 
8. 添加一个AddNum的方法，方法有两个输入参数(in)，一个输出参数(retval)，完成后，点击Next，Finish。
 
9. 可以在工程里搜索AddNum，看看哪些文件有所改变，以后也可以通过手动改变这些文件进行添加方法。
 
10. 在方法中输入代码，编译成功后再搜索AddNum字段，注意编译前保证VS是以管理员身份运行的，否则编译成功后组件自动注册失败。
 
11. 建立一个Exe程序MyClient，打开stdafx.h，引用上面生成的tlb文件。
 
12. 调用代码如下：

> 详见doc文档
 
13. 编译运行如下：


> 详见doc文档


 
14. 点击Configuration Manager：

> 详见doc文档
 
15. 如下图点击New，新建一个编译配置。

> 详见doc文档
  
16. 如下图点击New：

> 详见doc文档
 
17. 点击OK，完成一个64位编译的配置。

> 详见doc文档
 
18. 用新的配置编译，运行，结果如下：
 
> 详见doc文档

## 二， 自定义结构体数组传递参数

[http://blog.csdn.net/worldy/article/details/11850379](http://blog.csdn.net/worldy/article/details/11850379)

## 三，调sde数据
1. 无渲染调取
  Com 输入：连接参数
             图层名
       输出：坐标
            属性
   1. 以BSTR传递参数      ReadLayer
   2. 以SAFEARRAY传递参数  ReadLayerOneStr
2. 有渲染调取
 Com 输入：连接参数
            图层名
            渲染配置参数 
            过滤条件
       输出：BOOL
    1. 以BSTR传递参数      GetLyC
    2. 以SAFEARRAY传递参数  GetLyB
3. 报建通里调取
   AE方法调取：TestGetLy
  COM方法调取：TestGetLyB

   

