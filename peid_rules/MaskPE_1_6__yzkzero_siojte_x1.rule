rule _MaskPE_1_6__yzkzero_siojte
{
	meta:
		description = "MaskPE 1_6 __ yzkzero"
	strings:
		$a = {36812C24??????00C360}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
