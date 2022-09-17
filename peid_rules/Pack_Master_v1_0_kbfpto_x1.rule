rule _Pack_Master_v1_0_kbfpto
{
	meta:
		description = "Pack Master v1_0"
	strings:
		$a = {60E801??????E883C404E801??????E95D81EDD32240??E80402????E8EB08EB02CD20FF24249A66BE4746}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
