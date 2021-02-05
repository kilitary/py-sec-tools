rule _PEQuake_v0_06__forgotus_h__xhpzga
{
	meta:
		description = "PEQuake v0_06 __ forgotus _h_"
	strings:
		$a = {E8A50000002D??000000000000000000003D??00002D??000000000000000000000000000000000000000000004A??00005B??00006E??0000000000006B45724E654C33322E644C6C00000047657450726F634164}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
