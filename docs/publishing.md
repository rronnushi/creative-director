# Upload to GitHub

The GitHub upload ZIP contains the public repository files. The skill ZIP contains only the folder people install.

1. Extract `creative-director-github-upload-1.1.0.zip`.
2. Open [the repository](https://github.com/rronnushi/creative-director) and choose **Add file → Upload files**.
3. Upload the extracted contents, including `.github` and `.gitignore`. Don't upload the ZIP or an extra enclosing folder.
4. If version 1.0.0 was already uploaded, remove the old `creative-director` folder before uploading its replacement. GitHub file uploads don't remove files that are no longer in the new package. Also remove the old root `PUBLISHING.md` and `VALIDATION.md`; their replacements are in `docs/`.
5. Review the change and commit it. Check the **Actions** tab for actual validation results.

Personal profiles, private case studies, generated evaluation workspaces and local Git data are excluded. Keep them excluded when preparing your own archive.

For a release, attach `creative-director-1.1.0.zip` to the matching tag after checking the source and CI results. The release should describe the simpler wording and lighter package without claiming measured creative improvements.
