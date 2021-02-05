rule _LOCK98_V1_00_28__keenvim_esttrq
{
	meta:
		description = "LOCK98 V1_00_28 __ keenvim"
	strings:
		$a = {55E8000000005D81??????????EB05E9????????EB08}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
