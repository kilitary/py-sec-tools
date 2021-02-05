rule _tElock_v0_42_jdmjyk
{
	meta:
		description = "tElock v0_42"
	strings:
		$a = {C1EE00668BC9EB01EB60EB01EB9CE8000000005E83C6528BFE68790159EB01EBAC54E8035CEB08}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
