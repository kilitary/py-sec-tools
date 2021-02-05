rule _MoleBox_v2_3_0__Teggo_jpcxnu
{
	meta:
		description = "MoleBox v2_3_0 __ Teggo"
	strings:
		$a = {4204E8????0000A3??????008B4DF08B118915??????00??45FCA3??????005F5E8BE55DC3CCCCCCCCCCCCCCCCCCCCCCE8EBFBFFFF58E8??07000058894424206158FFD0E8????0000CCCCCCCCCCCCCC}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
