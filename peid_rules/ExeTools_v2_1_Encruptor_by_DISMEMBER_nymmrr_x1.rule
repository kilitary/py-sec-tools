rule _ExeTools_v2_1_Encruptor_by_DISMEMBER_nymmrr
{
	meta:
		description = "ExeTools v2_1 Encruptor by DISMEMBER"
	strings:
		$a = {E8????5D83????1E8CDA83????8EDA8EC2BB????BA????85D274}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
