rule _UPX_0_50__0_70_plunnb
{
	meta:
		description = "UPX 0_50 _ 0_70"
	strings:
		$a = {60E8000000005883E83D}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
