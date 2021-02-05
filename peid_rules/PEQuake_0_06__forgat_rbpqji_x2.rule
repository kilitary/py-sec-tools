rule _PEQuake_0_06__forgat_rbpqji
{
	meta:
		description = "PEQuake 0_06__ forgat"
	strings:
		$a = {E8A50000002D????0000000000000000003D????002D????0000000000000000000000000000000000000000004A????005B????006E????00000000006B45724E654C33322E644C6C00000047657450726F634164}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
