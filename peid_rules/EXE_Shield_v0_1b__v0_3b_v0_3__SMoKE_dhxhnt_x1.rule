rule _EXE_Shield_v0_1b__v0_3b_v0_3__SMoKE_dhxhnt
{
	meta:
		description = "EXE Shield v0_1b _ v0_3b_ v0_3 __ SMoKE"
	strings:
		$a = {E8040000008360EB0C5DEB05}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
