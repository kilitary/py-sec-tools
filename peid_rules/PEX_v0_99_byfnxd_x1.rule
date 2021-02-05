rule _PEX_v0_99_byfnxd
{
	meta:
		description = "PEX v0_99"
	strings:
		$a = {E9F5000000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
