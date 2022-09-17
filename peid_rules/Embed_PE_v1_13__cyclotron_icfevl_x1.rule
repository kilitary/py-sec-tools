rule _Embed_PE_v1_13__cyclotron_icfevl
{
	meta:
		description = "Embed PE v1_13 __ cyclotron"
	strings:
		$a = {83EC5060685DB9525AE82F990000DC99F3570568}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
