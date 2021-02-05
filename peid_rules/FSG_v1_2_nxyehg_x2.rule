rule _FSG_v1_2_nxyehg
{
	meta:
		description = "FSG v1_2"
	strings:
		$a = {4B45524E454C33322E646C6C00004C6F61644C69627261727941000047657450726F634164647265737300??0000000000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
