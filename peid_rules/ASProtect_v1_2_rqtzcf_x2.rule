rule _ASProtect_v1_2_rqtzcf
{
	meta:
		description = "ASProtect v1_2"
	strings:
		$a = {6801????00E801000000C3C3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
