# Exercise 8

9. below
   1. Res = **Proj**<sub>[eid]</sub> ( **Sel**<sub>[aname = 'Boeing 747']</sub> ( Aircraft **Join** Certified ) )

   2. Res = **Proj**<sub>[ename]</sub> ( **Sel**<sub>[aname = 'Boeing 747']</sub> ( Aircraft **Join**<sub>[aid=aircraft]</sub> ( Certified **Join**<sub>[employee=eid]</sub>Employees ) ) )

   3. Res = **Proj**<sub>[aid]</sub> ( **Sel**<sub>[cruisingRange>distance]</sub> ( Aircraft **Join** **Sel**<sub>[to='New York' and from 'Los Angeles']</sub> ( Flights ) ) )

   4. Tmp = **Proj**<sub>[flno, aid]</sub> ( **Sel**<sub>[cruisingRange>distance]</sub> ( Aircraft **Join** Flights ) ) <br>
   Res = **Proj**<sub>[flno]</sub> ( **Sel**<sub>[salary>100 000]</sub> ( Tmp **Join** Employees **Join** Certified ) )

   5. Tmp = **Proj**<sub>[cruisingDistance>3000]</sub>