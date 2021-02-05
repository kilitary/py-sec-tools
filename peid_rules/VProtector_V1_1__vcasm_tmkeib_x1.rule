rule _VProtector_V1_1__vcasm_tmkeib
{
	meta:
		description = "VProtector V1_1 __ vcasm"
	strings:
		$a = {B81AED4100B9ECEB41005051E874000000E8516A00005883E810B9B3000000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
