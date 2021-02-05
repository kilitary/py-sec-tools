rule _SDProtector_V1_1x__Randy_Li_zrwssk
{
	meta:
		description = "SDProtector V1_1x __ Randy Li"
	strings:
		$a = {558BEC6AFF68????????688888880864A1}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
