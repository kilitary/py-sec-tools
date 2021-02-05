rule _MS_Visual_C__v_8_DLL_h_small_sig2__imptba
{
	meta:
		description = "MS Visual C__ v_8 DLL _h_small sig2_"
	strings:
		$a = {8BFF558BEC538B5D08568B750C85F6578B7D100F84????000083FE01}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
