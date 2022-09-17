rule _MS_Visual_C__v_8_DLL_h_small_sig1__nosvap
{
	meta:
		description = "MS Visual C__ v_8 DLL _h_small sig1_"
	strings:
		$a = {8BFF558BEC837D0C017505E8??????FF5DE9D6FEFFFFCCCCCCCCCC}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
