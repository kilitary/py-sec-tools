rule _ASPack_v2_000_ntyjtr
{
	meta:
		description = "ASPack v2_000"
	strings:
		$a = {60E848110000C383}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
