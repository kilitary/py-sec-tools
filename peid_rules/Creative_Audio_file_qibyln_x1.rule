rule _Creative_Audio_file_qibyln
{
	meta:
		description = "Creative Audio file"
	strings:
		$a = {437265617469766520566F6963652046696C65}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
