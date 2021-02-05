rule _MSLRH_0_32a_fake_Microsoft_Visual_C____emadicius_wdsimf
{
	meta:
		description = "MSLRH 0_32a _fake Microsoft Visual C___ __ emadicius"
	strings:
		$a = {3BC074028183553BC074028183533BC97401BC563BD27402818557E8000000003BDB74019083C414EB05E8EB044000EBFAE80A000000E8EB0C0000E8F6FFFFFFE8F2FFFFFF83C40874047502EB02EB018150E80200}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
