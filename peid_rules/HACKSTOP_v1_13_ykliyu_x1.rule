rule _HACKSTOP_v1_13_ykliyu
{
	meta:
		description = "HACKSTOP v1_13"
	strings:
		$a = {52B8????1ECD2186E03D????73??CD200E1FB409E8????24??EA}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
