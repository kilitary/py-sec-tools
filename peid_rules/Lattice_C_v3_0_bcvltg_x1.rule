rule _Lattice_C_v3_0_bcvltg
{
	meta:
		description = "Lattice C v3_0"
	strings:
		$a = {FAB8????8ED8B8????8E}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
