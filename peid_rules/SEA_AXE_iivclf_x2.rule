rule _SEA_AXE_iivclf
{
	meta:
		description = "SEA_AXE"
	strings:
		$a = {FCBC????0E1FE8????26A1????8B1E????2BC38EC0B1??D3E3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
