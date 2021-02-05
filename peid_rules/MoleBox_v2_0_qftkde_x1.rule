rule _MoleBox_v2_0_qftkde
{
	meta:
		description = "MoleBox v2_0"
	strings:
		$a = {E8????????60E84F}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
