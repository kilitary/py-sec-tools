rule _HACKSTOP_v1_00_bnpajp
{
	meta:
		description = "HACKSTOP v1_00"
	strings:
		$a = {FABD????FFE56A49480C??E4??3F983F}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
