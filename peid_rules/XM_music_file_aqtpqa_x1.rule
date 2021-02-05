rule _XM_music_file_aqtpqa
{
	meta:
		description = "XM music file"
	strings:
		$a = {457874656E646564204D6F64756C653A}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
