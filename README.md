# data_driven_test
A project of data driven automation test practice.  
Step by step to build a data-driven automation test framework following the reference from: https://www.cnblogs.com/xiaxiaoxu/p/9297298.html  
What this project does is to login Salesforce and create an account.  

步骤1：搭建。  
创建test主程序，按过程罗列代码实现功能。  
步骤2：封装登录。  
新创建一个LoginPage类，在这个类下面创建一个login函数实现登录功能。将test主程序里面登录这一部分的代码移到LoginPage类下的login函数里面。在test主程序里面调用LoginPage类的login方法。  
步骤3：封装创建Account.  
新创建一个Account类，在这个类下面创建一个new_account函数实现新建account功能。将test主程序里面新建account这一部分的代码移到Account类下的new_account函数里面。在test主程序里面调用Account类的new_account方法。  
步骤4：封装查找元素的功能。  
将每一个元素的查找单独封装成一个方法。在登录过程中的每一步调用每个元素的查找方法并传递参数。  
步骤5：封装读取配置文件中数据的方法  
步骤6：用变量存储配置文件的路径  
步骤7：封装查找元素的功能和login功能的进一步封装  
步骤8：单独封装login方法  
步骤9：封装创建Account操作  
步骤10：单独封装创建Account的功能  
步骤11：封装excel操作  
新建test_data包，将维护测试数据的excel文件放置在该包下；在util包下新建ParseExcel类，封装对excel的操作；在主程序test中调用ParseExcel类读取excel文件中的测试数据并将测试数据传给login和new_account方法的参数。