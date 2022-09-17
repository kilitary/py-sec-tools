rule _ORiEN_v2_11_DEMO__ioziyd
{
	meta:
		description = "ORiEN v2_11 _DEMO_"
	strings:
		$a = {E95D010000CED1CECD0D}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
