rule _Microsoft_R_Full_text_index_file_byidtv
{
	meta:
		description = "Microsoft _R_ Full_text index file"
	strings:
		$a = {6C6C2D7465787420696E646578}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
