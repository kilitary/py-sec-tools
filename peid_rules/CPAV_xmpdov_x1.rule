rule _CPAV_xmpdov
{
	meta:
		description = "CPAV"
	strings:
		$a = {E8????4D5AB1019301000002}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
