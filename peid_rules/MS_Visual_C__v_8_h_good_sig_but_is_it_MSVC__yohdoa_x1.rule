rule _MS_Visual_C__v_8_h_good_sig_but_is_it_MSVC__yohdoa
{
	meta:
		description = "MS Visual C__ v_8 _h_good sig_ but is it MSVC__"
	strings:
		$a = {E8????????E98DFEFFFFCCCCCCCCCC66813D000000014D5A740433C0EB51A13C00000181B8000000015045000075EB0FB7881800000181F90B010000741B81F90B02000075D483B8840000010E76CB33C93988F800}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
