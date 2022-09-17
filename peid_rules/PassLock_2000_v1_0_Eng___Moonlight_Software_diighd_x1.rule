rule _PassLock_2000_v1_0_Eng___Moonlight_Software_diighd
{
	meta:
		description = "PassLock 2000 v1_0 _Eng_ __ Moonlight_Software"
	strings:
		$a = {558BEC535657BB00504000662EF7053420400004000F8598000000E81F01}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
