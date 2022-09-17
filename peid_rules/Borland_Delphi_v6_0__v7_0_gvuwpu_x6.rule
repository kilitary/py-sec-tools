rule _Borland_Delphi_v6_0__v7_0_gvuwpu
{
	meta:
		description = "Borland Delphi v6_0 _ v7_0"
	strings:
		$a = {558BEC83C4F0B8????????E8????????E8}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
