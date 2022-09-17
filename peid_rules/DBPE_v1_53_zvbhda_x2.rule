rule _DBPE_v1_53_zvbhda
{
	meta:
		description = "DBPE v1_53"
	strings:
		$a = {9C5557565251539CFAE8000000005D81ED5B534000B0}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
