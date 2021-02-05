rule _EmbedPE_1_13__cyclotron_dbyytl
{
	meta:
		description = "EmbedPE 1_13 __ cyclotron"
	strings:
		$a = {83EC5060685DB9525AE82F990000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
