rule _PE_Diminisher_v0_1_hzdamf
{
	meta:
		description = "PE Diminisher v0_1"
	strings:
		$a = {6A00E8????0000A3????4000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
