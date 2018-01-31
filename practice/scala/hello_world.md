# Hello world in scala

Link: http://tuxdna.in/files/presentations/scala-intro.html#slide1

```scala
scala> 1
res0: Int = 1

scala> 1.0
res1: Double = 1.0

scala> 'a'
res2: Char = a

scala> "a"
res3: String = a

scala> val a = 10
a: Int = 10

scala> a= 20
<console>:8: error: reassignment to val
       a= 20
        ^

scala> var b = 10
b: Int = 10

scala> b = 20
b: Int = 20

scala> val mylist = List(1,2,3,4)
mylist: List[Int] = List(1, 2, 3, 4)

scala> mylist.head
res4: Int = 1

scala> mylist.tail
res5: List[Int] = List(2, 3, 4)

scala> val myarray = Array(1.0, 4.0, 3.4)
myarray: Array[Double] = Array(1.0, 4.0, 3.4)

scala> val myarray2 = Array(1.0, 4.0, 3)
myarray2: Array[Double] = Array(1.0, 4.0, 3.0)

scala> val myarray3 = Array(1.0, 4.0, 'a')
myarray3: Array[Double] = Array(1.0, 4.0, 97.0)

scala> val myarray4 = Array(1.0, 4.0, "a")
myarray4: Array[Any] = Array(1.0, 4.0, a)

scala> myarray(4)
java.lang.ArrayIndexOutOfBoundsException: 4
	at .<init>(<console>:9)
	at .<clinit>(<console>)
	at .<init>(<console>:7)
	at .<clinit>(<console>)
	at $print(<console>)
	at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
	at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
	at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
	at java.lang.reflect.Method.invoke(Method.java:498)
	at scala.tools.nsc.interpreter.IMain$ReadEvalPrint.call(IMain.scala:734)
	at scala.tools.nsc.interpreter.IMain$Request.loadAndRun(IMain.scala:983)
	at scala.tools.nsc.interpreter.IMain.loadAndRunReq$1(IMain.scala:573)
	at scala.tools.nsc.interpreter.IMain.interpret(IMain.scala:604)
	at scala.tools.nsc.interpreter.IMain.interpret(IMain.scala:568)
	at scala.tools.nsc.interpreter.ILoop.reallyInterpret$1(ILoop.scala:760)
	at scala.tools.nsc.interpreter.ILoop.interpretStartingWith(ILoop.scala:805)
	at scala.tools.nsc.interpreter.ILoop.command(ILoop.scala:717)
	at scala.tools.nsc.interpreter.ILoop.processLine$1(ILoop.scala:581)
	at scala.tools.nsc.interpreter.ILoop.innerLoop$1(ILoop.scala:588)
	at scala.tools.nsc.interpreter.ILoop.loop(ILoop.scala:591)
	at scala.tools.nsc.interpreter.ILoop$$anonfun$process$1.apply$mcZ$sp(ILoop.scala:882)
	at scala.tools.nsc.interpreter.ILoop$$anonfun$process$1.apply(ILoop.scala:837)
	at scala.tools.nsc.interpreter.ILoop$$anonfun$process$1.apply(ILoop.scala:837)
	at scala.tools.nsc.util.ScalaClassLoader$.savingContextLoader(ScalaClassLoader.scala:135)
	at scala.tools.nsc.interpreter.ILoop.process(ILoop.scala:837)
	at scala.tools.nsc.MainGenericRunner.runTarget$1(MainGenericRunner.scala:83)
	at scala.tools.nsc.MainGenericRunner.process(MainGenericRunner.scala:96)
	at scala.tools.nsc.MainGenericRunner$.main(MainGenericRunner.scala:105)
	at scala.tools.nsc.MainGenericRunner.main(MainGenericRunner.scala)


scala> myarray(3)
java.lang.ArrayIndexOutOfBoundsException: 3
	at .<init>(<console>:9)
	at .<clinit>(<console>)
	at .<init>(<console>:7)
	at .<clinit>(<console>)
	at $print(<console>)
	at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
	at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
	at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
	at java.lang.reflect.Method.invoke(Method.java:498)
	at scala.tools.nsc.interpreter.IMain$ReadEvalPrint.call(IMain.scala:734)
	at scala.tools.nsc.interpreter.IMain$Request.loadAndRun(IMain.scala:983)
	at scala.tools.nsc.interpreter.IMain.loadAndRunReq$1(IMain.scala:573)
	at scala.tools.nsc.interpreter.IMain.interpret(IMain.scala:604)
	at scala.tools.nsc.interpreter.IMain.interpret(IMain.scala:568)
	at scala.tools.nsc.interpreter.ILoop.reallyInterpret$1(ILoop.scala:760)
	at scala.tools.nsc.interpreter.ILoop.interpretStartingWith(ILoop.scala:805)
	at scala.tools.nsc.interpreter.ILoop.command(ILoop.scala:717)
	at scala.tools.nsc.interpreter.ILoop.processLine$1(ILoop.scala:581)
	at scala.tools.nsc.interpreter.ILoop.innerLoop$1(ILoop.scala:588)
	at scala.tools.nsc.interpreter.ILoop.loop(ILoop.scala:591)
	at scala.tools.nsc.interpreter.ILoop$$anonfun$process$1.apply$mcZ$sp(ILoop.scala:882)
	at scala.tools.nsc.interpreter.ILoop$$anonfun$process$1.apply(ILoop.scala:837)
	at scala.tools.nsc.interpreter.ILoop$$anonfun$process$1.apply(ILoop.scala:837)
	at scala.tools.nsc.util.ScalaClassLoader$.savingContextLoader(ScalaClassLoader.scala:135)
	at scala.tools.nsc.interpreter.ILoop.process(ILoop.scala:837)
	at scala.tools.nsc.MainGenericRunner.runTarget$1(MainGenericRunner.scala:83)
	at scala.tools.nsc.MainGenericRunner.process(MainGenericRunner.scala:96)
	at scala.tools.nsc.MainGenericRunner$.main(MainGenericRunner.scala:105)
	at scala.tools.nsc.MainGenericRunner.main(MainGenericRunner.scala)


scala> myarray4(4)
java.lang.ArrayIndexOutOfBoundsException: 4
	at .<init>(<console>:9)
	at .<clinit>(<console>)
	at .<init>(<console>:7)
	at .<clinit>(<console>)
	at $print(<console>)
	at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
	at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
	at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
	at java.lang.reflect.Method.invoke(Method.java:498)
	at scala.tools.nsc.interpreter.IMain$ReadEvalPrint.call(IMain.scala:734)
	at scala.tools.nsc.interpreter.IMain$Request.loadAndRun(IMain.scala:983)
	at scala.tools.nsc.interpreter.IMain.loadAndRunReq$1(IMain.scala:573)
	at scala.tools.nsc.interpreter.IMain.interpret(IMain.scala:604)
	at scala.tools.nsc.interpreter.IMain.interpret(IMain.scala:568)
	at scala.tools.nsc.interpreter.ILoop.reallyInterpret$1(ILoop.scala:760)
	at scala.tools.nsc.interpreter.ILoop.interpretStartingWith(ILoop.scala:805)
	at scala.tools.nsc.interpreter.ILoop.command(ILoop.scala:717)
	at scala.tools.nsc.interpreter.ILoop.processLine$1(ILoop.scala:581)
	at scala.tools.nsc.interpreter.ILoop.innerLoop$1(ILoop.scala:588)
	at scala.tools.nsc.interpreter.ILoop.loop(ILoop.scala:591)
	at scala.tools.nsc.interpreter.ILoop$$anonfun$process$1.apply$mcZ$sp(ILoop.scala:882)
	at scala.tools.nsc.interpreter.ILoop$$anonfun$process$1.apply(ILoop.scala:837)
	at scala.tools.nsc.interpreter.ILoop$$anonfun$process$1.apply(ILoop.scala:837)
	at scala.tools.nsc.util.ScalaClassLoader$.savingContextLoader(ScalaClassLoader.scala:135)
	at scala.tools.nsc.interpreter.ILoop.process(ILoop.scala:837)
	at scala.tools.nsc.MainGenericRunner.runTarget$1(MainGenericRunner.scala:83)
	at scala.tools.nsc.MainGenericRunner.process(MainGenericRunner.scala:96)
	at scala.tools.nsc.MainGenericRunner$.main(MainGenericRunner.scala:105)
	at scala.tools.nsc.MainGenericRunner.main(MainGenericRunner.scala)


scala> myarray4(3)
java.lang.ArrayIndexOutOfBoundsException: 3
	at .<init>(<console>:9)
	at .<clinit>(<console>)
	at .<init>(<console>:7)
	at .<clinit>(<console>)
	at $print(<console>)
	at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
	at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
	at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
	at java.lang.reflect.Method.invoke(Method.java:498)
	at scala.tools.nsc.interpreter.IMain$ReadEvalPrint.call(IMain.scala:734)
	at scala.tools.nsc.interpreter.IMain$Request.loadAndRun(IMain.scala:983)
	at scala.tools.nsc.interpreter.IMain.loadAndRunReq$1(IMain.scala:573)
	at scala.tools.nsc.interpreter.IMain.interpret(IMain.scala:604)
	at scala.tools.nsc.interpreter.IMain.interpret(IMain.scala:568)
	at scala.tools.nsc.interpreter.ILoop.reallyInterpret$1(ILoop.scala:760)
	at scala.tools.nsc.interpreter.ILoop.interpretStartingWith(ILoop.scala:805)
	at scala.tools.nsc.interpreter.ILoop.command(ILoop.scala:717)
	at scala.tools.nsc.interpreter.ILoop.processLine$1(ILoop.scala:581)
	at scala.tools.nsc.interpreter.ILoop.innerLoop$1(ILoop.scala:588)
	at scala.tools.nsc.interpreter.ILoop.loop(ILoop.scala:591)
	at scala.tools.nsc.interpreter.ILoop$$anonfun$process$1.apply$mcZ$sp(ILoop.scala:882)
	at scala.tools.nsc.interpreter.ILoop$$anonfun$process$1.apply(ILoop.scala:837)
	at scala.tools.nsc.interpreter.ILoop$$anonfun$process$1.apply(ILoop.scala:837)
	at scala.tools.nsc.util.ScalaClassLoader$.savingContextLoader(ScalaClassLoader.scala:135)
	at scala.tools.nsc.interpreter.ILoop.process(ILoop.scala:837)
	at scala.tools.nsc.MainGenericRunner.runTarget$1(MainGenericRunner.scala:83)
	at scala.tools.nsc.MainGenericRunner.process(MainGenericRunner.scala:96)
	at scala.tools.nsc.MainGenericRunner$.main(MainGenericRunner.scala:105)
	at scala.tools.nsc.MainGenericRunner.main(MainGenericRunner.scala)


scala> myarray4
res10: Array[Any] = Array(1.0, 4.0, a)

scala> myarray4(2)
res11: Any = a

scala> myarray4(2).getType
<console>:9: error: value getType is not a member of Any
              myarray4(2).getType
                          ^

scala> myarray4(2).getClass
res13: Class[_] = class java.lang.String

scala> myarray4(1).getClass
res14: Class[_] = class java.lang.Double

scala> val mylist2 = List(1,2,3,"a")
mylist2: List[Any] = List(1, 2, 3, a)

scala> myarray4.
apply          asInstanceOf   clone          isInstanceOf   length         toString       update         

scala> myarray4.apply(1)
res15: Any = 4.0

scala> myarray4(1)
res16: Any = 4.0

scala> a
res17: Int = 10

scala> mylist
res18: List[Int] = List(1, 2, 3, 4)

scala> mylist.map(x => x*2)
res19: List[Int] = List(2, 4, 6, 8)

scala> val mymap = Map("java" -> "good", "c" -> "awesome", "python" -> "amazing")
mymap: scala.collection.immutable.Map[String,String] = Map(java -> good, c -> awesome, python -> amazing)

scala> val mymap2 = Map("java" -> 2, 2.0 -> "awesome", 'a' -> "amazing")
mymap2: scala.collection.immutable.Map[Any,Any] = Map(java -> 2, 2.0 -> awesome, a -> amazing)

scala> mymap2("awesome")
java.util.NoSuchElementException: key not found: awesome
	at scala.collection.MapLike$class.default(MapLike.scala:228)
	at scala.collection.AbstractMap.default(Map.scala:58)
	at scala.collection.MapLike$class.apply(MapLike.scala:141)
	at scala.collection.AbstractMap.apply(Map.scala:58)
	at .<init>(<console>:9)
	at .<clinit>(<console>)
	at .<init>(<console>:7)
	at .<clinit>(<console>)
	at $print(<console>)
	at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
	at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
	at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
	at java.lang.reflect.Method.invoke(Method.java:498)
	at scala.tools.nsc.interpreter.IMain$ReadEvalPrint.call(IMain.scala:734)
	at scala.tools.nsc.interpreter.IMain$Request.loadAndRun(IMain.scala:983)
	at scala.tools.nsc.interpreter.IMain.loadAndRunReq$1(IMain.scala:573)
	at scala.tools.nsc.interpreter.IMain.interpret(IMain.scala:604)
	at scala.tools.nsc.interpreter.IMain.interpret(IMain.scala:568)
	at scala.tools.nsc.interpreter.ILoop.reallyInterpret$1(ILoop.scala:760)
	at scala.tools.nsc.interpreter.ILoop.interpretStartingWith(ILoop.scala:805)
	at scala.tools.nsc.interpreter.ILoop.command(ILoop.scala:717)
	at scala.tools.nsc.interpreter.ILoop.processLine$1(ILoop.scala:581)
	at scala.tools.nsc.interpreter.ILoop.innerLoop$1(ILoop.scala:588)
	at scala.tools.nsc.interpreter.ILoop.loop(ILoop.scala:591)
	at scala.tools.nsc.interpreter.ILoop$$anonfun$process$1.apply$mcZ$sp(ILoop.scala:882)
	at scala.tools.nsc.interpreter.ILoop$$anonfun$process$1.apply(ILoop.scala:837)
	at scala.tools.nsc.interpreter.ILoop$$anonfun$process$1.apply(ILoop.scala:837)
	at scala.tools.nsc.util.ScalaClassLoader$.savingContextLoader(ScalaClassLoader.scala:135)
	at scala.tools.nsc.interpreter.ILoop.process(ILoop.scala:837)
	at scala.tools.nsc.MainGenericRunner.runTarget$1(MainGenericRunner.scala:83)
	at scala.tools.nsc.MainGenericRunner.process(MainGenericRunner.scala:96)
	at scala.tools.nsc.MainGenericRunner$.main(MainGenericRunner.scala:105)
	at scala.tools.nsc.MainGenericRunner.main(MainGenericRunner.scala)


scala> mymap2
res21: scala.collection.immutable.Map[Any,Any] = Map(java -> 2, 2.0 -> awesome, a -> amazing)

scala> mymap2(2.0)
res22: Any = awesome

scala> mymap2(2.0).getClass
res23: Class[_] = class java.lang.String

scala> mymap2.apply(2.0)
res24: Any = awesome

scala> import scala.collectaion.mutable
<console>:7: error: object collectaion is not a member of package scala
       import scala.collectaion.mutable
                    ^

scala> import scala.collection.mutable
import scala.collection.mutable

scala> mymap2(2.0) = "not-awesome"
<console>:10: error: value update is not a member of scala.collection.immutable.Map[Any,Any]
              mymap2(2.0) = "not-awesome"
              ^

scala> val mymap3 = mutable.Map("java" -> 2, 2.0 -> "awesome", 'a' -> "amazing")
mymap3: scala.collection.mutable.Map[Any,Any] = Map(2.0 -> awesome, a -> amazing, java -> 2)

scala> mymap3
res26: scala.collection.mutable.Map[Any,Any] = Map(2.0 -> awesome, a -> amazing, java -> 2)

scala> val tuple3 = ('a', 1, "name")
tuple3: (Char, Int, String) = (a,1,name)

scala> tuple3.
_1                _2                _3                asInstanceOf      canEqual          copy              isInstanceOf      productArity      productElement    
productIterator   productPrefix     toString          

scala> tuple3.product
productArity      productElement    productIterator   productPrefix     

scala> tuple3.productArity 
res27: Int = 3

scala> tuple3._2
res28: Int = 1

scala> tuple3._3
res29: String = name

scala> import java.util.Calendar
import java.util.Calendar

scala> val now = Calendar.getInstance()
now: java.util.Calendar = java.util.GregorianCalendar[time=1517265262115,areFieldsSet=true,areAllFieldsSet=true,lenient=true,zone=sun.util.calendar.ZoneInfo[id="Asia/Kolkata",offset=19800000,dstSavings=0,useDaylight=false,transitions=6,lastRule=null],firstDayOfWeek=1,minimalDaysInFirstWeek=1,ERA=1,YEAR=2018,MONTH=0,WEEK_OF_YEAR=5,WEEK_OF_MONTH=5,DAY_OF_MONTH=30,DAY_OF_YEAR=30,DAY_OF_WEEK=3,DAY_OF_WEEK_IN_MONTH=5,AM_PM=0,HOUR=4,HOUR_OF_DAY=4,MINUTE=4,SECOND=22,MILLISECOND=115,ZONE_OFFSET=19800000,DST_OFFSET=0]

scala> val hour = now.get(Calendar.HOUR_OF_DAY)
hour: Int = 4

scala> println( if(hour < 12) "good afternoon" else "good morning")
good afternoon

scala> val dow = now.get(Calendar.DAY_OF_WEEK)
dow: Int = 3

scala> dow match {
     |         case 1 => "Sunday"
     |         case 2 => "Monday"
     |         case 3 => "Tuesday"
     |         case 4 => "Wednesday"
     |         case 5 => "Thursday"
     |         case 6 => "Friday"
     |         case 7 => "Saturday"
     |        }
res31: String = Tuesday

scala> dow match {
     |  case x: String => "dow is a string"
     | case x: Double => "dow is a double"
     | case _ => "don't know yet"
     | }
<console>:13: error: scrutinee is incompatible with pattern type;
 found   : String
 required: Int
               case x: String => "dow is a string"
                       ^
<console>:14: error: scrutinee is incompatible with pattern type;
 found   : Double
 required: Int
              case x: Double => "dow is a double"

```
