rule _tElock_v0_4x__v0_5x_rnpmty
{
	meta:
		description = "tElock v0_4x _ v0_5x"
	strings:
		$a = {C1EE00668BC9EB01EB60EB01EB9CE8000000005E83C65E8BFE68790159EB01EBAC54E8035CEB08}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
