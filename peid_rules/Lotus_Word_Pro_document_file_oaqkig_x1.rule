rule _Lotus_Word_Pro_document_file_oaqkig
{
	meta:
		description = "Lotus Word Pro document file"
	strings:
		$a = {576F726450726F??????????????????4C575037}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
