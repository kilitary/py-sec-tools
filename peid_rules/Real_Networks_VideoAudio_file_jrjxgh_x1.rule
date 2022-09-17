rule _Real_Networks_VideoAudio_file_jrjxgh
{
	meta:
		description = "Real Networks VideoAudio file"
	strings:
		$a = {2E524D46}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
