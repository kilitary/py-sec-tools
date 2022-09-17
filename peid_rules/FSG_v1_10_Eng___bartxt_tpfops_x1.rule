rule _FSG_v1_10_Eng___bartxt_tpfops
{
	meta:
		description = "FSG v1_10 _Eng_ __ bartxt"
	strings:
		$a = {80E9A1C1C11368E4167546C1C1055EEB019D6864863746EB028CE05FF7D0}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
