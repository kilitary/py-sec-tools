rule _ASPack_v1_08_03_ebbrlz
{
	meta:
		description = "ASPack v1_08_03"
	strings:
		$a = {60E8000000005D????????????BB????????03DD}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
