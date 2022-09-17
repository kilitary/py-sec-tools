rule _Pelles_C_2_x_4_x_DLL__Pelle_Orinius_vkjyfy
{
	meta:
		description = "Pelles C 2_x_4_x DLL __ Pelle Orinius"
	strings:
		$a = {5589E55356578B5D0C8B7510}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
