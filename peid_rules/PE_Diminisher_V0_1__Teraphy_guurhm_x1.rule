rule _PE_Diminisher_V0_1__Teraphy_guurhm
{
	meta:
		description = "PE Diminisher V0_1 __ Teraphy"
	strings:
		$a = {535152565755E800000000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
