rule _NoodleCrypt_v2_0_ourldm
{
	meta:
		description = "NoodleCrypt v2_0"
	strings:
		$a = {060E0E071FE800005B83EB08BA270103D3E83C02BAEA}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
